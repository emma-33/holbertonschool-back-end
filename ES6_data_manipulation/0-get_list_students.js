export default function getListStudents() {
  const students = [];

  students.push({
    id: 1,
    firstName: 'Guillaume',
    location: 'San Fransisco',
  });

  students.push({
    id: 2,
    firstName: 'James',
    location: 'Columbia',
  });

  students.push({
    id: 5,
    firstName: 'Serena',
    location: 'San Fransisco',
  });

  return students;
}
