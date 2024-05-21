export default function getStudentsIdsSum(listOfStudents) {
  return listOfStudents.reduce((sum, student) => sum + student.id, 0);
}
