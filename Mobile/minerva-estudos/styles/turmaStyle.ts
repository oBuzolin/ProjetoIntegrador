import { StyleSheet } from "react-native";

const turmaStyles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
  },
  header: {
    flexDirection: "row",
    alignItems: "center",
    padding: 10,
    backgroundColor: "#e3e3e3",
  },
  logo: {
    width: 40,
    height: 40,
    marginRight: 10,
  },
  headerText: {
    fontSize: 18,
    fontWeight: "bold",
  },
  cardTurma: {
    flexDirection: "row",
    backgroundColor: "#f0f0f0",
    margin: 10,
    borderRadius: 8,
    padding: 10,
    alignItems: "center",
  },
  turmaImagem: {
    width: 60,
    height: 60,
    borderRadius: 30,
    marginRight: 10,
  },
  cardInfo: {
    flex: 1,
    justifyContent: "space-between",
    flexDirection: "row",
    alignItems: "center",
  },
  cardNome: {
    fontSize: 18,
    fontWeight: "bold",
  },
  input: {
    margin: 10,
    padding: 10,
    borderColor: "#ccc",
    borderWidth: 1,
    borderRadius: 8,
  },
  mural: {
    flex: 1,
    paddingHorizontal: 10,
  },
  mensagemContainer: {
    marginBottom: 10,
    padding: 10,
    backgroundColor: "#f8f8f8",
    borderRadius: 8,
  },
  footer: {
    flexDirection: "row",
    justifyContent: "space-around",
    backgroundColor: "#e3e3e3",
    paddingVertical: 10,
  },
  footerButton: {
    alignItems: "center",
  },
  footerText: {
    alignItems: "center",
    fontSize: 12,
    color: "teal",
  },
});

export default turmaStyles;
