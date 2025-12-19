from datetime import date

from app.extensions import db
from app.models.experience import Experience


def _experience_payload(**overrides):
    payload = {
        "title": "Automation Project",
        "category": "project",
        "description": "Automates reporting",
        "start_date": "2024-01-01",
        "link": "https://example.com",
    }
    payload.update(overrides)
    return payload


def _create_experience():
    experience = Experience(
        title="Existing project",
        category="project",
        description="Already in DB",
        start_date=date(2023, 1, 1),
        link="https://example.com",
    )
    db.session.add(experience)
    db.session.commit()
    return experience


def test_admin_create_experience(client, admin_headers):
    response = client.post(
        "/api/v1/admin/experience",
        headers=admin_headers,
        json=_experience_payload(),
    )

    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Automation Project"
    assert data["public"] is True


def test_admin_update_experience(client, admin_headers, app):
    with app.app_context():
        experience = _create_experience()
        experience_id = experience.id

    response = client.put(
        f"/api/v1/admin/experience/{experience_id}",
        headers=admin_headers,
        json={"public": False},
    )

    assert response.status_code == 200
    data = response.get_json()
    assert data["public"] is False
    with app.app_context():
        updated = Experience.query.get(experience_id)
        assert updated.public is False


def test_admin_delete_experience(client, admin_headers, app):
    with app.app_context():
        experience = _create_experience()
        experience_id = experience.id

    response = client.delete(
        f"/api/v1/admin/experience/{experience_id}",
        headers=admin_headers,
    )

    assert response.status_code == 204
    with app.app_context():
        assert Experience.query.get(experience_id) is None


def test_admin_requires_valid_token(client):
    response = client.post(
        "/api/v1/admin/experience",
        headers={"X-Admin-Token": "wrong-token", "Content-Type": "application/json"},
        json=_experience_payload(),
    )

    assert response.status_code == 401

