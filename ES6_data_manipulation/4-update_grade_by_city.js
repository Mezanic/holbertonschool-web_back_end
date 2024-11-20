export default function updateStudentGradeByCity(arrayStudents, city, newGrade) {
  return arrayStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrade.find((newGrade) => newGrade.studentId === student.id);

      const updateStudent = { ...student };
      if (grade) {
        updateStudent.grade = grade.grade;
      } else {
        updateStudent.grade = 'N/A';
      }
      return updateStudent;
    });
}
