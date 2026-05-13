from user import User
from post import Post

app_user_one = User("jd@ja.com", "Juli", "pwd", "DevOps engineer")
app_user_one.get_user_info()

app_user_two = User("boby@com", "Robert", "pwd", "Agent")
app_user_two.get_user_info()

new_post = Post("You are my sun shine ", app_user_two.name)
new_post.get_post_info()