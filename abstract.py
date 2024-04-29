from abc import abstractmethod


class Dataprocessor:

  @abstractmethod
  def read_data(self, data):
    pass

  def write_data(self, data):
    pass

  class csvprocessor:

    def read_data(self, data):
      with open(data, "+r") as file:
        print(file.read())

    def read_data(self, data):
      with open(data, "+w") as file:
        print(file.write(input()))
