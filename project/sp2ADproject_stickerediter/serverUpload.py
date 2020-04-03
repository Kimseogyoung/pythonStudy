#서버／블로그에　업로드　코드

import xmlrpc.client
import ftplib
import os

API_URL = 'https://api.blog.naver.com/xmlrpc'


class NaverBlog(object):
    def __init__(self, user_id, api_key):
        self.__server = None
        self.__user_id = user_id
        self.__api_key = api_key
        self.__categories = []

        try:
            self.__set_categories()
        except Exception as e:
            raise e

    def __client(self):
        if self.__server is None:
            self.__server = xmlrpc.client.ServerProxy(API_URL)

        return self.__server

    def __set_categories(self):
        categories = self.__client().metaWeblog.getCategories(self.__user_id,
                                                              self.__user_id,
                                                              self.__api_key)

        for category in categories:
            self.__categories.append(category['title'])

    def post(self, title, description, category, publish=True):
        struct = {}
        struct['title'] = title
        struct['description'] = description
        if category in self.__categories:
            struct['categories'] = [category]

        try:
            return self.__client().metaWeblog.newPost(self.__user_id,
                                                      self.__user_id,
                                                      self.__api_key,
                                                      struct,
                                                      publish)
        except Exception as e:
            raise e


def serverupload(filename):

    #나의　사진파일　cafe 24서버에　업로드하기
    #filename = "test1.png"
    ftp = ftplib.FTP()
    ftp.connect("my ftp adress")  # Ftp 주소 Connect(주소 , 포트)
    ftp.login("id", "password")  # login (ID, Password)
    ftp.cwd("ftp adress")  # 파일 전송할 Ftp 주소 (받을 주소)
    os.chdir("my file adress")  # 파일 전송 대상의 주소(보내는 주소)
    myfile = open(filename, 'rb')  # Open( ~ ,'r') <= Text파일은 됨, Open( ~ ,'rb') <= 이미지파일 됨
    ftp.storbinary('STOR ' + filename, myfile)

    myfile.close()
    ftp.close()
    #닫기



