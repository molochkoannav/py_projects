from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_mixin_print_init(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    result = capsys.readouterr()
    assert result.out == "Product(Iphone 15 , 512GB, Gray space, 210000.0, 8)\n"
    Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    result = capsys.readouterr()
    assert result.out == "Smartphone(Iphone 15 , 512GB, Gray space, 210000.0, 8)\n"
    LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    result = capsys.readouterr()
    assert result.out == "LawnGrass(Газонная трава , Элитная трава для газона, 500.0, 20)\n"
