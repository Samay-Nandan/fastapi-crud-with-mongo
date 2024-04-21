from bson import ObjectId


def object_id_to_string(obj: ObjectId):
    """Converts ObjectId to string if the object is an instance of ObjectId."""
    return str(obj) if isinstance(obj, ObjectId) else None


custom_encoders = {
    ObjectId: object_id_to_string,
}
