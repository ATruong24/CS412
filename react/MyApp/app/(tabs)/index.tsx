import { View, Text, Image } from 'react-native';
import { styles } from '../../assets/my_styles';

export default function IndexScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.titleText}>React Project</Text>

      <Text style={styles.bodyText}>
        This is my index page! Below is a picture of me and I currently applying to internships. This picture was taken last year by my wonderful roommate!
      </Text>

      <Image
        source={require('../../assets/images/me.jpg')}
        style={styles.localImage}
      />
    </View>
  );
}