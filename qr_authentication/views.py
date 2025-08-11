import io
import qrcode
import base64
from .models import TemporaryId, QRAuthSession
from .serializers import TemporaryIdSerializer, QRAuthSessionSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

# webapp generates qrcode containing a unique code for the webapp

class GenerateTemporaryId(APIView):
    def post(self, request, *args, **kwargs):
        # Step 1: Create the temporary id
        temp = TemporaryId.objects.create()

        # Step 2: Generate the QR code
        qr_img = qrcode.make(str(temp.temp_id))

        # Step 3: Store QR in memory
        buffer = io.BytesIO()
        qr_img.save(buffer, format="PNG")
        # buffer.seek(0)

        # Step 4: Convert to Base64
        qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        # Step 5: Return as JSON
        return Response({
            # "temp_id": str(temp.temp_id),
            "qr": qr_base64
        })

