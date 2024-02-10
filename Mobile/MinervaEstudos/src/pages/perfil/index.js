import { View, StyleSheet, Text } from "react-native";

export function Perfil() {
  return (
    <View styles={styles.container}>
      <Text>Pagina Perfil</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
