import { View, Text, Image } from 'react-native';
import { styles } from '../../assets/my_styles';

export default function IndexScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}>TODO: Your Title</Text>

      <Text style={styles.bodyText}>
        TODO: A few sentences about you (or one of your interests).
      </Text>

      {/* Local image: put the file in MyApp/assets/images/ and update the name.
          require() paths must be static strings. */}
      <Image
        source={require('../../assets/images/me.jpg')}
        style={styles.localImage}
      />
    </View>
  );
}