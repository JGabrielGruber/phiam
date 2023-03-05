import hug
from controllers import user

router = hug.route.API(__name__)

router.get('/')(user.get_users)
router.post('/')(user.add_user)
router.get('/{uuid}')(user.get_user)
router.put('/{uuid}')(user.update_user)
router.delete('/{uuid}')(user.delete_user)
