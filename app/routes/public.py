from flask import Blueprint, request, jsonify
from app.models.experience import Experience
from app.schemas.experience_schema import ExperienceSchema
from app.models.timeline import Timeline
from app.schemas.timeline_schema import TimelineSchema

public_bp = Blueprint('public', __name__, url_prefix='/api/v1')

@public_bp.route('/experience', methods=['GET'])
def list_experience():
    schema = ExperienceSchema(many=True)
    ## Только публичные записи
    query = Experience.query.filter_by(public = True)

    ## Фильтрация по категории
    category = request.args.get('category')
    if category:
        query = query.filter_by(category=category)

    ## Фильтрация по тегу
    tag = request.args.get('tag')
    if tag:
        query = query.filter(Experience.tags.contains([tag]))

    ## Сортировка по дате начала
    experiences = query.order_by(Experience.start_date.desc()).all()
    return jsonify(schema.dump(experiences))

@public_bp.route('/timeline', methods=['GET'])
def list_timeline():
    schema = TimelineSchema(many=True)
    query = Timeline.query

    order_dir = request.args.get('order', 'desc').lower()
    ## Определяем направление сортировки (по умолчанию - от новых к старым)
    if order_dir == 'asc':
        query = query.order_by(Timeline.order.asc().nullslast(), Timeline.date.asc())
    else:
        query = query.order_by(Timeline.order.desc().nullslast(), Timeline.date.desc())

    limit = request.args.get('limit', type=int)
    if limit is None or limit <= 0:
        limit = 10

    offset = request.args.get('offset', type=int)

    query = query.limit(limit)
    if offset:
        query = query.offset(offset)

    timelines = query.all()
    return jsonify(schema.dump(timelines))

