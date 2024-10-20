import pytest
from src.constants.api_constants import APIConstants

class TestUsers:
    @pytest.fixture(autouse=True)
    def setup(self, api_helper):
        self.api_helper = api_helper
        self.constants = APIConstants
    
    def test_list_users(self):
        """Test to verify listing users with pagination"""
        response = self.api_helper.get(
            self.constants.USERS_ENDPOINT,
            params={"page": 2}
        )
        
        assert response.status_code == self.constants.SUCCESS_CODE
        data = response.json()
        assert "page" in data
        assert "data" in data
        assert len(data["data"]) > 0
    
    def test_create_user(self):
        """Test to verify user creation"""
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = self.api_helper.post(
            self.constants.USERS_ENDPOINT,
            payload
        )
        
        assert response.status_code == self.constants.CREATED_CODE
        data = response.json()
        assert data["name"] == payload["name"]
        assert data["job"] == payload["job"]
        assert "id" in data
        assert "createdAt" in data