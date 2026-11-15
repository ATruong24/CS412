import { StyleSheet } from 'react-native';

// Shared styles for all screens. Tweak colors/sizes to make it your own.
export const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#ffffff',
  },
  scrollContainer: {
    alignItems: 'center',
    padding: 20,
    backgroundColor: '#ffffff',
  },
  titleText: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 12,
    textAlign: 'center',
  },
  bodyText: {
    fontSize: 16,
    lineHeight: 22,
    marginVertical: 10,
    textAlign: 'center',
  },
  localImage: {
    width: 250,
    height: 250,
    borderRadius: 12,
    marginTop: 12,
  },
  remoteImage: {
    width: 300,
    height: 200,
    borderRadius: 8,
    marginVertical: 10,
  },
});