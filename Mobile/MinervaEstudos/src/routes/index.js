import { createBottomTabNavigator } from 'react-native-paper/react-navigation';
import { MaterialCommunityIcons } from '@expo/vector-icons';

import { Materias } from '../pages/materias'
import { Pendentes } from '../pages/pendentes' 
import { Perfil } from '../pages/perfil'
import { Ranking } from '../pages/ranking'

const Tab = createBottomTabNavigator();

export function Routes() {
     return( 
        <Tab.Navigator>
            <Tab.Screen name="Materias" component={Materias} />
            <Tab.Screen name="Pendentes" component={Pendentes} />
            <Tab.Screen name="Ranking" component={Ranking} /> 
            <Tab.Screen name="Perfil" component={Perfil} />
        </Tab.Navigator>
    );
}