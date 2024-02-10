import "react-native-gesture-handler";
import { Materias } from "../pages/materias";
import { Pendentes } from "../pages/pendentes";
import { Ranking } from "../pages/ranking";
import { Perfil } from "../pages/perfil";

import { createDrawerNavigator } from "@react-navigation/drawer";
import { createAppContainer } from "@react-navigation/native";

const MenuLateral = createDrawerNavigator({
  Perfil: {
    screen: Perfil,
  },
  Matérias: {
    screen: Materias,
  },
  Pendentes: {
    screen: Pendentes,
  },
});

export default createAppContainer(MenuLateral);
