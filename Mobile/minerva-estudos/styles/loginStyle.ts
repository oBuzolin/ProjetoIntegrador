import { StyleSheet } from "react-native";

const loginStyles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#1E1E1E",
    alignItems: "center",
    justifyContent: "center",
    paddingHorizontal: 20,
  },
  welcomeText: {
    fontSize: 24,
    color: "#FFF",
    marginBottom: 10,
  },
  signInText: {
    color: "#FFF",
    marginBottom: 20,
  },
  input: {
    width: "100%",
    backgroundColor: "#333",
    borderRadius: 8,
    padding: 15,
    color: "#FFF",
    marginBottom: 15,
  },
  forgotPassword: {
    color: "#888",
    alignSelf: "flex-end",
    marginBottom: 20,
  },
  signInButton: {
    width: "100%",
    backgroundColor: "#3C6EFD",
    padding: 15,
    borderRadius: 8,
    alignItems: "center",
    marginBottom: 15,
  },
  signInButtonText: {
    color: "#FFF",
    fontSize: 16,
  },
  logo: {
    width: 350,
    height: 350,
  },
});

export default loginStyles;
