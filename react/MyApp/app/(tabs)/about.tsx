import { View, Text, Image } from 'react-native';
import { styles } from '../../assets/my_styles';

export default function AboutScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}>About Me</Text>
      <Image
        source={{ uri: 'https://cs-people.bu.edu/atruong4/images/pizza.jpg' }}
        style={styles.remoteImage}
      />

      <Text style={styles.bodyText}>
        Hello, my name is Anthony and I'm currently a Junior at Boston University studying Computer Science. I enjoy going out to eat and trying new foods. 
      </Text>
    </View>
  );
}