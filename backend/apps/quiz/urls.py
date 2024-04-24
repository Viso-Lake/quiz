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
router.register("admin", AdminViewSet)
router.register("answer", AnswerViewSet)
router.register("feedback", FeedbackViewSet)
router.register("history", HistoryViewSet)
router.register("options", OptionsViewSet)
router.register("questions", QuestionsViewSet)
router.register("quiz", QuizViewSet)
router.register("rank", RankViewSet)
router.register("user", UserViewSet)

# Включаем созданные роуты в urlpatterns
urlpatterns = [
    path("", include(router.urls)),
]
