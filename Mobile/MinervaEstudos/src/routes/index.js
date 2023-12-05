import { createBottomNavigation } from "@react-navigation/bottom-tabs";

import { Materias } from "../pages/materias";
import { Pendentes } from "../pages/pendentes";
import { Perfil } from "../pages/perfil";
import { Ranking } from "../pages/ranking"; 

const Tab = createBottomNavigation();

export function Routes() {
    return(
        <Tab.Navigator>        
            <Tab.Screen name="Materias" component={Materias}/>
            <Tab.Screen name="Pendentes" component={Pendentes}/>
            <Tab.Screen name="Ranking" component={Ranking}/>
            <Tab.Screen name="Perfil" component={Perfil}/>
        <Tab.Navigator/>
    );
}
