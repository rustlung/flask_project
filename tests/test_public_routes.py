from datetime import date

from app.extensions import db
from app.models.experience import Experience
from app.models.timeline import Timeline


def _create_experience():
    experience = Experience(
        title="Public Project",
        category="project",
        description="Demo project for tests",
        start_date=date(2024, 1, 1),
        end_date=date(2024, 3, 1),
        highlights=["API", "docs"],
        tags=["Flask", "Showcase"],
        public=True,
        link="https://example.com",
    )
    db.session.add(experience)
    db.session.commit()
    return experience


def _create_timeline():
    first = Timeline(
        date=date(2023, 1, 1),
        title="Started learning Flask",
        description="Built first API",
        category="learning",
        order=1,
        highlight=True,
    )
    second = Timeline(
        date=date(2023, 6, 1),
        title="Built showcase",
        description="Designed resume hub",
        category="project",
        order=2,
        highlight=False,
    )
    db.session.add_all([first, second])
    db.session.commit()
    return first, second


def test_list_experience_returns_public_entries(client, app):
    with app.app_context():
        experience = _create_experience()
        expected_title = experience.title
        expected_category = experience.category

    response = client.get("/api/v1/experience")

    assert response.status_code == 200
    payload = response.get_json()
    assert isinstance(payload, list)
    assert payload[0]["title"] == expected_title
    assert payload[0]["category"] == expected_category


def test_list_timeline_can_limit_and_sort(client, app):
    with app.app_context():
        first, second = _create_timeline()
        expected_title = second.title

    response = client.get("/api/v1/timeline?limit=1")

    assert response.status_code == 200
    payload = response.get_json()
    assert len(payload) == 1
    # Default order is descending by order, so second (order=2) should come first
    assert payload[0]["title"] == expected_title

