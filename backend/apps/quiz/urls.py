from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AdminViewSet,
    AnswerViewSet,
    FeedbackViewSet,
    HistoryViewSet,
    OptionsViewSet,
    QuestionsViewSet,
    QuizViewSet,
    RankViewSet,
    UserViewSet,
)

# Создаем экземпляр DefaultRouter
router = DefaultRouter()

# Регистрируем все viewsets
router.register("admins", AdminViewSet)
router.register("answers", AnswerViewSet)
router.register("feedbacks", FeedbackViewSet)
router.register("histories", HistoryViewSet)
router.register("options", OptionsViewSet)
router.register("questions", QuestionsViewSet)
router.register("quizes", QuizViewSet)
router.register("ranks", RankViewSet)
router.register("users", UserViewSet)

# Включаем созданные роуты в urlpatterns
urlpatterns = [
    path("", include(router.urls)),
]
