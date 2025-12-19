from marshmallow import Schema, fields, validate, post_load
from app.models.experience import Experience

class ExperienceSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=160))
    category = fields.Str(
        required=True,
        validate=validate.OneOf(['project', 'role', 'certificate'])
    )
    description = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(allow_none=True, load_default=None)
    highlights = fields.List(fields.Str(), load_default=list, allow_none=True)
    tags = fields.List(fields.Str(), load_default=list, allow_none=True)
    public = fields.Bool(load_default=True)
    link = fields.Url(required=False, allow_none=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @post_load
    def make_experience(self, data, **kwargs):
        if kwargs.get("partial"):
            return data
        return Experience(**data)