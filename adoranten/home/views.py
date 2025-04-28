from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from wagtail.models import Page


class SubmitFormAPIView(APIView):
    def post(self, request, page_id):

        try:
            page = Page.objects.get(id=page_id).specific
        except Page.DoesNotExist:
            return Response({"error": "Page not found."},
                            status=status.HTTP_404_NOT_FOUND)

        form = page.get_form(request.data)

        if form.is_valid():
            page.process_form_submission(form)
            return Response({"message": page.thank_you_text},
                            status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
