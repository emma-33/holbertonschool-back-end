export default function cleanSet(set, startString) {
  const newString = [];

  if (!startString || startString.length === 0) {
    return '';
  }

  for (const element of set) {
    if (element && element.startsWith(startString)) {
      newString.push(element.slice(startString.length));
    }
  }
  return newString.join('-');
}
