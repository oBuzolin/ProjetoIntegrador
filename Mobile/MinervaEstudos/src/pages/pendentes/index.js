import { View, StyleSheet, Text } from "react-native";

export function Pendentes() {
  return (
    <View styles={styles.container}>
      <Text>Pagina Pendentes</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
});
