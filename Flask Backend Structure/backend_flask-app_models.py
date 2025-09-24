from datetime import datetime

class User:
    def __init__(self, id, name, email, age, location, interests, bio, created_at=None):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.location = location
        self.interests = interests
        self.bio = bio
        self.created_at = created_at or datetime.utcnow()
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'location': self.location,
            'interests': self.interests,
            'bio': self.bio,
            'created_at': self.created_at.isoformat()
        }

class Match:
    def __init__(self, user1_id, user2_id, score, matched_at=None):
        self.user1_id = user1_id
        self.user2_id = user2_id
        self.score = score
        self.matched_at = matched_at or datetime.utcnow()
