from pprint import pprint

from google.cloud import storage

def run():
    LOCAL_PATH = "/Users/Jesse/smartdoor/new"

    def get_file_path(user_name, image_id):

        return "{0}/{1}.jpg".format(user_name, image_id)

    def get_local_path(image_id):
        return "{0}/{1}.jpg".format(LOCAL_PATH, image_id)


    client = storage.Client(project="crested-guru-170618")

    bucket = client.get_bucket('images-smartdoor')

    # # Then do other things...
    #  blob = bucket.get_blob('remote/path/to/file.txt')
    # print(blob.download_as_string())
    # blob.upload_from_string('New contents!')

    user_name = "jesse"
    image_id = "face_pic_4"

    blob = bucket.blob(get_file_path(user_name, image_id))
    response = blob.upload_from_filename(filename=get_local_path(image_id))
    bucket.make_public(recursive=True)
