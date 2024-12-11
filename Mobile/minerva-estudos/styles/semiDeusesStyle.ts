import { StyleSheet } from "react-native";

const semiDeusesStyles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  header: {
    padding: 16,
    backgroundColor: "#f8f8f8",
    borderBottomWidth: 1,
    borderBottomColor: "#ddd",
  },
  headerText: {
    fontSize: 18,
    fontWeight: "bold",
  },
  scrollView: {
    flex: 1,
  },
  sectionTitle: {
    fontSize: 16,
    fontWeight: "bold",
    marginVertical: 8,
    marginLeft: 16,
  },
  userRow: {
    flexDirection: "row",
    alignItems: "center",
    padding: 16,
    borderBottomWidth: 1,
    borderBottomColor: "#ddd",
  },
  userText: {
    flex: 1,
    marginLeft: 8,
    fontSize: 16,
  },
  footer: {
    flexDirection: "row",
    borderTopWidth: 1,
    borderTopColor: "#ddd",
    backgroundColor: "#f8f8f8",
  },
  footerButton: {
    flex: 1,
    alignItems: "center",
    padding: 16,
  },
  footerText: {
    marginTop: 4,
    fontSize: 12,
  },
});

export default semiDeusesStyles;
