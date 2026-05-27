from unittest.mock import patch

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

from characters.models import Character
from characters.serializers import CharacterSerializer


class CharacterViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_character_filter_by_name(self):
        character_1 = Character.objects.create(
            api_id="1",
            name="Character 1",
            status="Alive",
            species="Species 1",
            gender="Male",
            image="http://test.com/test.jpg"
        )
        character_2 = Character.objects.create(
            api_id="2",
            name="Character 2",
            status="Alive",
            species="Species 2",
            gender="Male",
            image="http://test.com/test.jpg"
        )

        response = self.client.get(
            reverse("characters:character_list"),
            data={"name": "Character 1"}
        )
        serializer_1 = CharacterSerializer(character_1)
        serializer_2 = CharacterSerializer(character_2)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_1.data, response.data)
        self.assertNotEqual(serializer_2.data, response.data)

    @patch("characters.views.random.choice")
    def test_get_random_character(self, mock_choice):
        character = Character.objects.create(
            api_id="1",
            name="Rick",
            status="Alive",
            species="Human",
            gender="Male",
            image="http://test.com/test.jpg"
        )

        mock_choice.return_value = character.pk

        response = self.client.get(
            reverse("characters:random_character")
        )

        serializer = CharacterSerializer(character)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)