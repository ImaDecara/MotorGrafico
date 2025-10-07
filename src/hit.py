from pyglm import glm

class Hit:
    def __init__(self, get_model_matrix, hittable = True):
        self.__model_matrix = get_model_matrix
        self.hittable = hittable

    @property
    def model_matrix(self):
        return self.__model_matrix()

    @property
    def position(self):
        m = self.model_matrix
        return glm.vec3(m[3].x, m[3].y, m[3].z)

    @property
    def scale(self):
        m = self.model_matrix
        return glm.vec3(
            glm.length(glm.vec3(m[0])),
            glm.length(glm.vec3(m[1])),
            glm.length(glm.vec3(m[2])))

    def check_hit(self, origin, direction):
        raise NotImplementedError("Subclasses must implement this method")


class HitBox(Hit):
    def __init__(self, get_model_matrix, hittable = True):
        super().__init__(get_model_matrix, hittable)

    def check_hit(self, origin, direction):
        if(not self.hittable):
            return False
    
    
        origin = glm.vec3(origin)
        direction = glm.normalize(glm.vec3(direction))

        min_bounds = self.position - self.scale
        max_bounds = self.position + self.scale

        tmin = (min_bounds - origin) / direction
        tmax = (max_bounds - origin) / direction

        t1 = glm.min(tmin, tmax)
        t2 = glm.max(tmin, tmax)

        v1 = glm.vec3(*t1)
        v2 = glm.vec3(*t2)
        
        t_near = max(v1.x, v1.y, v1.z)
        t_far = min(v2.x, v2.y, v2.z)

        return t_near <= t_far and t_far >= 0