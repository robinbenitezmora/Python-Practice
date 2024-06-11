// Masks
$(document).ready(function(){
    $('#student_cpf').mask('000.000.000-00');
    $('#student_affiliation1_cpf').mask('000.000.000-00');
    $('#student_affiliation2_cpf').mask('000.000.000-00');
    $('#teacher_cpf').mask('000.000.000-00');
  });
  
  $(document).ready(function(){
    $('#student_new certificate').mask('000000 00 00 0000 0 00000 000 0000000 00');
  });
  
  $(document).ready(function(){
    $('#student_cep_residence').mask('00000-000');
    $('#teacher_cep_residence').mask('00000-000');
  });
  
  $(document).ready(function(){
    $('#student_birth_date').mask('00/00/0000');
    $('#teacher_birth_date').mask('00/00/0000');
  });
  
  
  // Cokie Consent
  window.cookieconsent.initialise({
    "palette": {
      "popup": {
        "background": "#102d69"
      },
      "button": {
        "background": "#FBBA00"
      }
    },
    "theme": "classic",
  });