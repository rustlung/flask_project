from flask import Blueprint, request, jsonify, current_app
from marshmallow import ValidationError
from app.extensions import db
from app.models.experience import Experience
from app.models.timeline import Timeline
from app.schemas.experience_schema import ExperienceSchema
from app.schemas.timeline_schema import TimelineSchema

admin_bp = Blueprint('admin', __name__, url_prefix='/api/v1/admin')

## -------------------- Experience --------------------
## Создание опыта
@admin_bp.route('/experience', methods=['POST'])
def create_experience():
    ## 1. Проверяем токен
    token = request.headers.get('X-Admin-Token')
    if token != current_app.config['ADMIN_TOKEN']:
        return jsonify({'error': 'Unauthorized'}), 401
    
    ## 2. Валидация данных
    schema = ExperienceSchema()
    try:
        experience = schema.load(request.get_json())
    except ValidationError as exc:
        return jsonify({'error': 'Validation error', 'details': exc.messages}), 400
    
    ## 3. Сохраняем данные
    db.session.add(experience)
    db.session.commit()

    ## 4. Отдаем созданный объект
    return jsonify(schema.dump(experience)), 201

## Обновление опыта
@admin_bp.route('/experience/<int:id>', methods=['PUT'])
def update_experience(id):
    ## 1. Проверяем токен
    token = request.headers.get('X-Admin-Token')
    if token != current_app.config['ADMIN_TOKEN']:
        return jsonify({'error': 'Unauthorized'}), 401
    
    ## 2. Получаем объект
    schema = ExperienceSchema()
    experience = Experience.query.get_or_404(id)
    try:
        validated_data = schema.load(request.get_json(), partial=True)
    except ValidationError as exc:
        return jsonify({'error': 'Validation error', 'details': exc.messages}), 400
    
    ## 3. Обновляем данные
    for key, value in validated_data.items():
        setattr(experience, key, value)
    db.session.commit()

    ## 4. Отдаем обновленный объект
    return jsonify(schema.dump(experience)), 200


## Удаление опыта
@admin_bp.route('/experience/<int:id>', methods=['DELETE'])
def delete_experience(id):
    ## 1. Проверяем токен
    token = request.headers.get('X-Admin-Token')
    if token != current_app.config['ADMIN_TOKEN']:
        return jsonify({'error': 'Unauthorized'}), 401
    
    ## 2. Получаем объект
    experience = Experience.query.get_or_404(id)
    db.session.delete(experience)
    db.session.commit()

    ## 3. Отдаем успешный ответ
    return jsonify({'message': 'Experience deleted successfully'}), 204

## -------------------- Timeline --------------------
## Создание события
@admin_bp.route('/timeline', methods=['POST'])
def create_timeline():
    ## 1. Проверяем токен
    token = request.headers.get('X-Admin-Token')
    if token != current_app.config['ADMIN_TOKEN']:
        return jsonify({'error': 'Unauthorized'}), 401
    
    ## 2. Валидация данных
    schema = TimelineSchema()
    try:
        timeline = schema.load(request.get_json())
    except ValidationError as exc:
        return jsonify({'error': 'Validation error', 'details': exc.messages}), 400
    
    ## 3. Сохраняем данные
    db.session.add(timeline)
    db.session.commit()

    ## 4. Отдаем созданный объект
    return jsonify(schema.dump(timeline)), 201

## Обновление события
@admin_bp.route('/timeline/<int:id>', methods=['PUT'])
def update_timeline(id):
    ## 1. Проверяем токен
    token = request.headers.get('X-Admin-Token')
    if token != current_app.config['ADMIN_TOKEN']:
        return jsonify({'error': 'Unauthorized'}), 401

    ## 2. Получаем объект
    schema = TimelineSchema()
    timeline = Timeline.query.get_or_404(id)
    try:
        validated_data = schema.load(request.get_json(), partial=True)
    except ValidationError as exc:
        return jsonify({'error': 'Validation error', 'details': exc.messages}), 400
    
    ## 3. Обновляем данные
    for key, value in validated_data.items():
        setattr(timeline, key, value)
    db.session.commit()

    ## 4. Отдаем обновленный объект
    return jsonify(schema.dump(timeline)), 200

## Удаление события
@admin_bp.route('/timeline/<int:id>', methods=['DELETE'])
def delete_timeline(id):
    ## 1. Проверяем токен
    token = request.headers.get('X-Admin-Token')
    if token != current_app.config['ADMIN_TOKEN']:
        return jsonify({'error': 'Unauthorized'}), 401
    
    ## 2. Получаем объект
    timeline = Timeline.query.get_or_404(id)
    db.session.delete(timeline)
    db.session.commit()

    ## 3. Отдаем успешный ответ
    return jsonify({'message': 'Timeline deleted successfully'}), 204