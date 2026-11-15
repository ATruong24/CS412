import { View, Text, Image } from 'react-native';
import { styles } from '../../assets/my_styles';

export default function AboutScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}>TODO: About</Text>

      {/* Can be a local require(...) or a remote { uri: ... } image */}
      <Image
        source={{ uri: 'https://cs-people.bu.edu/USERNAME/images/about.jpg' }}
        style={styles.remoteImage}
      />

      <Text style={styles.bodyText}>
        TODO: "About" text — who made this app, for what class, etc.
      </Text>
    </View>
  );
}