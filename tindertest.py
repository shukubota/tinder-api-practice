import pynder
import time
facebook_auth_token = "EAAGm0PX4ZCpsBALWIsvePP79CRRMmZBJdKkm0dHhnblManiehnZBkHoac6PivANBPZA7WSWhriOLqiY25KDgKDZCioqM7np2UxJmKOmSfZCkmRgF8YtyBI3ISjjCZBrhh3189f7mZBwMb0OZAWop7R11xsVHxczXKPjFMIhuZAY1PY11kkp5wJDvu5GteOJg3bJlJZCxd4UZChUyr68NoB4DaXKSLdjQZCs8YgbAaAslbOqCLoOpb4SZCNvTCPUWl6xZAogum0ZD"

LAT = 35.687537
LON = 139.529551
session = pynder.Session(facebook_auth_token)
users = session.nearby_users()
matchs = session.matches()
session.update_location(LAT, LON)
friends = session.get_fb_friends()

user_info_objects = []
# for friend in friends:
#   user_info_objects.append(friend.get_tinder_information())
# print(user_info_objects)

# for match in matchs:
#   try:
#     print(match)
#   except:
#     pass

# print(session)
# print(users)
# print(session.profile)
# print(matchs)

count = 0
start = time.time()
for user in users:
  count += 1
  print(count)
  elapsed_time = time.time() - start
  print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
  if count > 200000000:
    break

  try:
    a=user.like()
    # print(a)
    print(user.bio)
    if len(user.schools):
      continue
    print(user.name)
    # print(user.photos)
    for photo in user.photos:
      print(photo)
    # print(user.thumbnail)
    # print(user.birth_date)
    # print(user.age)
    # print(user.ping_time)
    # print(user.distance_km )
    # print(user.common_connections)
    # print(user.common_interests)
    # print(user.instagram_username)
    # print(user.instagram_photos)
    # print(user.schools)
    # print(len(user.schools))
    # print(user.jobs)
  except:
    # pass
    # traceback.print_exc()
    print('例外')

