class Vertex:
    def __init__(self, name, format, array):
        self.__name = name
        self.__format = format
        self.__array = array

    @property
    def get_name(self):
        return self.__name

    @property
    def get_format(self):
        return self.__format
    
    @property
    def get_array(self):
        return self.__array

class VertexLayout:
    def __init__(self):
        self.__vertices = []

    def add_attribute(self, name: str, format: str, array):
        self.__vertices.append(Vertex(name, format, array))

    def get_attributes(self):
        return self.__vertices
    
class Model:
    def __init__(self, vetices = None, indices = None, colors = None, normals = None, texcords = None):
        self.indices = indices
        self.vertex_layout = VertexLayout()
        if vetices is not None:
            self.vertex_layout.add_attribute("in_pos", "3f", vetices)
        if colors is not None:
            self.vertex_layout.add_attribute("in_color", "3f", colors)
        if normals is not None:
            self.vertex_layout.add_attribute("in_normal", "3f", normals)
        if texcords is not None:
            self.vertex_layout.add_attribute("in_texcoord", "2f", texcords)