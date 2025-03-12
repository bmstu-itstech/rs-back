from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginationMeta:
    """
    Метакласс для создания пагинаторов с заданной величиной
    размера страницы page_size.

    Используется просто:
        pagination_class = PaginationMeta(page_size=16)

    Почему так сложно? Django требует передачи класса, а не его объекта;
    то есть сделать CommonPagination с параметром page_size в конструкторе нельзя.
    Поэтому мы создаём метакласс, который имитирует конструктор, а внутри вызывает
    настоящий с требуемым параметром.
    """

    class _CommonPagination(PageNumberPagination):
        # GET-запрос будет возвращать за раз не более чем
        # page_size записей
        page_size: int

        def __init__(self, page_size: int = 8, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.page_size = page_size

        def get_paginated_response(self, data):
            return Response({
                'results': data,
                'previous': self.get_previous_link(),
                'next': self.get_next_link(),
                'count': self.page.paginator.count,
                'page_size': self.page_size,
            })

    page_size: int

    def __init__(self, page_size: int = 8):
        self.page_size = page_size

    def __call__(self, *args, **kwargs):
        c = self._CommonPagination(self.page_size, *args, **kwargs)
        c.page_size = self.page_size
        return c
