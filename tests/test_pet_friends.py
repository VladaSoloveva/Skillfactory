from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=""):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_invalid_age(name='Том', animal_type='кот', age='7', pet_photo='cat.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name


def test_delete_pet_valid_key(pet_id='287339'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, pet_id)
    assert status == 200
    assert result['pet_id'] == pet_id


def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
   _, auth_key = pf.get_api_key(valid_email, valid_password)
   _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

   if len(my_pets['pets']) > 0:
       status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
       assert status == 200
       assert result['name'] == name
   else:
       raise Exception("There is no my pets")

