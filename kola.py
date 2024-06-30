# Шаг 1: Создание класса ГорячийНапиток
public class ГорячийНапиток {
    private String name;
    private int volume;

    public ГорячийНапиток(String name, int volume) {
        this.name = name;
        this.volume = volume;
    }

    public String getName() {
        return name;
    }

    public int getVolume() {
        return volume;
    }

    @Override
    public String toString() {
        return "ГорячийНапиток{" +
                "name='" + name + '\'' +
                ", volume=" + volume +
                '}';
    }
}

# Шаг 2: Создание наследника ГорячийНапиток с дополнительным полем температура
public class ГорячийНапитокСТемпературой extends ГорячийНапиток {
    private int температура;

    public ГорячийНапитокСТемпературой(String name, int volume, int температура) {
        super(name, volume);
        this.температура = температура;
    }

    public int getТемпература() {
        return температура;
    }

    @Override
    public String toString() {
        return "ГорячийНапитокСТемпературой{" +
                "name='" + getName() + '\'' +
                ", volume=" + getVolume() +
                ", температура=" + температура +
                '}';
    }
}

# Шаг 3: Создание интерфейса ТорговыйАвтомат
public interface ТорговыйАвтомат {
    ГорячийНапитокСТемпературой getProduct(String name, int volume, int температура);
}

# Шаг 4: Создание класса ГорячихНапитковАвтомат, реализующего интерфейс ТорговыйАвтомат
import java.util.ArrayList;
import java.util.List;

public class ГорячихНапитковАвтомат implements ТорговыйАвтомат {
    private List<ГорячийНапитокСТемпературой> напитки = new ArrayList<>();

    public void добавитьНапиток(ГорячийНапитокСТемпературой напиток) {
        напитки.add(напиток);
    }

    @Override
    public ГорячийНапитокСТемпературой getProduct(String name, int volume, int температура) {
        for (ГорячийНапитокСТемпературой напиток : напитки) {
            if (напиток.getName().equals(name) && напиток.getVolume() == volume && напиток.getТемпература() == температура) {
                return напиток;
            }
        }
        return null; // или можно выбросить исключение, если напиток не найден
    }
}

# Шаг 5: Создание main метода и инициализация объектов
public class Main {
    public static void main(String[] args) {
        ГорячихНапитковАвтомат автомат = new ГорячихНапитковАвтомат();

        автомат.добавитьНапиток(new ГорячийНапитокСТемпературой("Кофе", 200, 80));
        автомат.добавитьНапиток(new ГорячийНапитокСТемпературой("Чай", 250, 75));
        автомат.добавитьНапиток(new ГорячийНапитокСТемпературой("Какао", 300, 85));

        ГорячийНапитокСТемпературой напиток = автомат.getProduct("Чай", 250, 75);
        if (напиток != null) {
            System.out.println("Вы получили: " + напиток);
        } else {
            System.out.println("Такого напитка нет.");
        }
    }
}