import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Image,
  Alert,
} from "react-native";
import loginStyles from "@/styles/loginStyle";
import { useRouter } from "expo-router";

const styles = loginStyles;

const index: React.FC = () => {
  // Estados para capturar o usuário e senha
  const [usuario, setUsuario] = useState("");
  const [senha, setSenha] = useState("");

  const router = useRouter();
  // Função para enviar os dados ao backend
  const handleLogin = async () => {
    if (!usuario || !senha) {
      Alert.alert("Erro", "Por favor, preencha todos os campos!");
      return;
    }

    router.push("/professorHome");
  };
  //   try {
  //     // Chamada ao backend em NestJS
  //     const response = await axios.post("http://localhost:3000/auth/login", {
  //       usuario,
  //       senha,
  //     });

  //     // Sucesso na autenticação
  //     Alert.alert("Sucesso", response.data.message);
  //     console.log("Token recebido:", response.data.token); // Salve o token se necessário
  //   } catch (error) {
  //     console.error("Erro no login:", error);
  //     Alert.alert(
  //       "Erro",
  //       "Falha ao realizar o login. Verifique suas credenciais."
  //     );
  //   }
  // };

  return (
    <View style={styles.container}>
      <Image source={require("../images/livro.png")} style={styles.logo} />
      <Text style={styles.welcomeText}>Bem vindo!</Text>
      <Text style={styles.signInText}>Por favor faça login com sua conta</Text>

      <TextInput
        placeholder="Email"
        placeholderTextColor="#999"
        style={styles.input}
        value={usuario}
        onChangeText={setUsuario}
      />
      <TextInput
        placeholder="Senha"
        placeholderTextColor="#999"
        secureTextEntry
        style={styles.input}
        value={senha}
        onChangeText={setSenha}
      />

      <TouchableOpacity style={styles.signInButton} onPress={handleLogin}>
        <Text style={styles.signInButtonText}>Entrar</Text>
      </TouchableOpacity>
    </View>
  );
};

export default index;
