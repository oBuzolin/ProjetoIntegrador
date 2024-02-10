import "react-native-gesture-handler";
import { NavigationContainer } from "@react-navigation/native";
import { Routes } from "./src/routes";
import Navigator from "./src/routes/drawer";

export default function App() {
  return (
    <NavigationContainer>
      <Navigator />
    </NavigationContainer>
  );
}
