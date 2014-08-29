import unittest
import random
from filesystems import filesystem
import os

class FileTest(unittest.TestCase):

	f = '';

	def setUp(self):
		self.f = Filesystem();
		directory = './files/'

		if os.path.exists(directory):
			self.f.deleteDir(directory)

		if not os.path.exists(directory):
			self.f.createDir(directory)

    	self.f.write('file.txt', 'contents')

	def tear_down(self):
		self.f.delete('file.txt')
		self.f.deleteDir('files')

	def get_file(self):
		self.f.get('files.txt')

	def test_read(self):
		_file = self.get_file()
		_contents = _file.read()
		self.assertEqual(_contents, 'contents')

	def test_read_stream(self):
		_file = self.get_file();

if __name__ == "__main__":
	unittest.main()