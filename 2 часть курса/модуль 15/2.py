import math

class MyMath:
    @staticmethod
    def circle_len(radius: float) -> float:
        """
        Вычисляет длину окружности.

        Args:
        - radius (float): Радиус окружности

        Returns:
        - float: Длина окружности
        """
        return 2 * math.pi * radius

    @staticmethod
    def circle_sq(radius: float) -> float:
        """
        Вычисляет площадь окружности.

        Args:
        - radius (float): Радиус окружности

        Returns:
        - float: Площадь окружности
        """
        return math.pi * (radius ** 2)

    @staticmethod
    def cube_volume(side_length: float) -> float:
        """
        Вычисляет объем куба.

        Args:
        - side_length (float): Длина стороны куба

        Returns:
        - float: Объем куба
        """
        return side_length ** 3

    @staticmethod
    def sphere_surface_area(radius: float) -> float:
        """
        Вычисляет площадь поверхности сферы.

        Args:
        - radius (float): Радиус сферы

        Returns:
        - float: Площадь поверхности сферы
        """
        return 4 * math.pi * (radius ** 2)


circle_len_result = MyMath.circle_len(5)
circle_sq_result = MyMath.circle_sq(6)
print(circle_len_result)
print(circle_sq_result)