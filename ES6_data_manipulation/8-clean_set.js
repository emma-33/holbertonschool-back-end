export default function cleanSet(set, startString) {
  const newString = [];

  if (startString.length === 0) {
    return '';
  }

  for (const element of set) {
    if (element.startsWith(startString)) {
      newString.push(element.slice(startString.length));
    }
  }
  return newString.join('-');
}
