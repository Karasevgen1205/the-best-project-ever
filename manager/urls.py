from django.urls import path
from manager.views import MyPage, AddCommentLike, BookDetail, AddRate2Book, AddBook, LoginView, \
    logout_user, AddComment, book_delete, UpdateBook


urlpatterns = [
    path('add_like_comment/<str:slug>', AddCommentLike.as_view(), name="add-like-comment"),
    path('add_like_comment/<str:slug>/<str:location>/', AddCommentLike.as_view(), name="add-like-comment-location"),
    path("add_rate_to_book/<str:slug>/<int:rate>/", AddRate2Book.as_view(), name="add-rate"),
    path("add_rate_to_book/<str:slug>/<int:rate>/<str:location>/", AddRate2Book.as_view(), name="add-rate-location"),
    path("book_view_detail/<str:slug>/", BookDetail.as_view(), name="book-detail"),
    path("add_book/", AddBook.as_view(), name="add-book"),
    path("add_comment/<str:slug>/", AddComment.as_view(), name="add-comment"),
    path("delete_book/<str:slug>/", book_delete, name="delete-book"),
    path("update_book/<str:slug>/", UpdateBook.as_view, name="update-book"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("", MyPage.as_view(), name="the-main-page"),
]