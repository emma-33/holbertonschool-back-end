export default function updateStudentGradeByCity(listOfStudents, city, newGrades) {
  const filteredStudents = listOfStudents.filter((student) => student.location === city);

  return filteredStudents.map((student) => {
    const filteredGrades = newGrades.find((grade) => grade.studentId === student.id);
    let grade;

    if (filteredGrades) {
      grade = filteredGrades.grade;
    } else {
      grade = 'N/A';
    }
    return { ...student, grade };
  });
}
