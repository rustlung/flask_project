from marshmallow import Schema, fields, validate, post_load
from app.models.timeline import Timeline

class TimelineSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=160))
    description = fields.Str(required=True)
    category = fields.Str(
        required=False,
        validate=validate.OneOf(['learning', 'project', 'role', 'certificate']),
        allow_none=True,
        load_default=None
    )
    highlight = fields.Bool(required=False, load_default=False)
    order = fields.Int(required=False, allow_none=True, load_default=None)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @post_load
    def make_timeline(self, data, **kwargs):
        if kwargs.get("partial"):
            return data
        return Timeline(**data)