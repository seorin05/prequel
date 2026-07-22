# app/models/__init__.py
from app.core.database import Base
from .user import User
from .content import KContent, LiteraryWork
from .tag import Tag, KContentTag, LiteraryWorkTag
from .recommendation import Favorite, Recommendation
from .additional_info import Translation, VisualAid