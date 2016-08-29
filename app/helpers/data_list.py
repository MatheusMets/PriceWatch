
def get_brands_list():
  return ['acer', 'asus', 'apple', 'dell', 'hp', 'samsung']



class DataList:

  def is_valid_brand(self, string=""):
    return (string.lower() in get_brands_list())

  def get_brands_regex():
    return '/' + '|'.join(map(str, get_brands_list())) + '/'
