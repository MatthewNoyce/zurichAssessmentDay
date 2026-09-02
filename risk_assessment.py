"""
Risk Assessment Module for Life Insurance Applications.
Calculates risk scores based on health, lifestyle, and other factors.
"""

class RiskAssessment:
    """Calculate risk scores for life insurance applications."""
    
    @staticmethod
    def calculate_risk_score(application_data):
        """
        Calculate overall risk score from complete application data.
        Returns a dictionary with score, decision, and breakdown.
        """
        score = 0
        breakdown = {}
        
        # Extract data sections
        health = application_data.get('healthAndMedicalHistory', {})
        lifestyle = application_data.get('lifestyleAndDrivingHistory', {})
        financial = application_data.get('financialAndAdditionalInformation', {})
        personal = application_data.get('personalInformation', {})
        
        # Calculate BMI score
        bmi_score = RiskAssessment._calculate_bmi_score(health)
        score += bmi_score
        breakdown['bmi'] = bmi_score
        
        # Calculate medical conditions score
        medical_score = RiskAssessment._calculate_medical_score(health)
        score += medical_score
        breakdown['medical_conditions'] = medical_score
        
        # Calculate smoking score
        smoking_score = RiskAssessment._calculate_smoking_score(lifestyle)
        score += smoking_score
        breakdown['smoking'] = smoking_score
        
        # Calculate alcohol score
        alcohol_score = RiskAssessment._calculate_alcohol_score(lifestyle)
        score += alcohol_score
        breakdown['alcohol'] = alcohol_score
        
        # Calculate drug use score
        drug_score = RiskAssessment._calculate_drug_score(lifestyle)
        score += drug_score
        breakdown['drugs'] = drug_score
        
        # Calculate hazardous activities score
        hazard_score = RiskAssessment._calculate_hazard_score(lifestyle)
        score += hazard_score
        breakdown['hazardous_activities'] = hazard_score
        
        # Calculate driving history score
        driving_score = RiskAssessment._calculate_driving_score(lifestyle)
        score += driving_score
        breakdown['driving_history'] = driving_score
        
        # Calculate criminal history score
        criminal_score = RiskAssessment._calculate_criminal_score(financial)
        score += criminal_score
        breakdown['criminal_history'] = criminal_score
        
        # Calculate previous declination score
        declination_score = RiskAssessment._calculate_declination_score(financial)
        score += declination_score
        breakdown['previous_declination'] = declination_score
        
        # Determine decision based on total score
        decision = RiskAssessment._determine_decision(score)
        
        return {
            'total_score': score,
            'decision': decision,
            'breakdown': breakdown,
            'risk_level': RiskAssessment._get_risk_level(score)
        }
    
    @staticmethod
    def _calculate_bmi_score(health_data):
        """Calculate risk score based on BMI."""
        try:
            bmi = float(health_data.get('bmi', 0))
            if bmi == 0:
                return 0
            
            if bmi < 18.5:  # Underweight
                return 15
            elif 18.5 <= bmi < 25:  # Normal
                return 0
            elif 25 <= bmi < 30:  # Overweight
                return 10
            elif 30 <= bmi < 35:  # Obese Class I
                return 25
            elif 35 <= bmi < 40:  # Obese Class II
                return 40
            else:  # Obese Class III
                return 60
        except (ValueError, TypeError):
            return 0
    
    @staticmethod
    def _calculate_medical_score(health_data):
        """Calculate risk score based on medical conditions."""
        score = 0
        
        # Check for serious conditions in medical history
        conditions = health_data.get('medicalConditions', '').lower()
        
        high_risk_conditions = ['cancer', 'heart disease', 'stroke', 'diabetes', 'kidney disease']
        moderate_risk_conditions = ['asthma', 'high blood pressure', 'hypertension', 'cholesterol']
        
        for condition in high_risk_conditions:
            if condition in conditions:
                score += 50
        
        for condition in moderate_risk_conditions:
            if condition in conditions:
                score += 20
        
        # Check family history
        family_history = health_data.get('familyHistory', '').lower()
        if family_history and family_history != 'none':
            for condition in high_risk_conditions:
                if condition in family_history:
                    score += 15
        
        # Check mental health
        mental_health = health_data.get('mentalHealth', '').lower()
        if mental_health and mental_health != 'none':
            if 'depression' in mental_health or 'anxiety' in mental_health:
                score += 10
        
        # Check surgeries
        surgeries = health_data.get('surgeries', '').lower()
        if surgeries and surgeries != 'none':
            score += 10
        
        return score
    
    @staticmethod
    def _calculate_smoking_score(lifestyle_data):
        """Calculate risk score based on smoking habits."""
        smoker = lifestyle_data.get('smoker', 'no')
        
        if smoker == 'yes':
            return 40
        elif smoker == 'former':
            return 15
        else:
            return 0
    
    @staticmethod
    def _calculate_alcohol_score(lifestyle_data):
        """Calculate risk score based on alcohol consumption."""
        alcohol = lifestyle_data.get('alcohol', 'none')
        
        alcohol_scores = {
            'none': 0,
            'occasional': 0,
            'moderate': 5,
            'regular': 15,
            'heavy': 35
        }
        
        return alcohol_scores.get(alcohol, 0)
    
    @staticmethod
    def _calculate_drug_score(lifestyle_data):
        """Calculate risk score based on drug use."""
        drugs = lifestyle_data.get('drugs', 'no')
        
        if drugs == 'yes':
            return 100  # Immediate refer
        elif drugs == 'former':
            return 30
        else:
            return 0
    
    @staticmethod
    def _calculate_hazard_score(lifestyle_data):
        """Calculate risk score based on hazardous activities."""
        hazardous = lifestyle_data.get('hazardousActivities', 'no')
        
        if hazardous == 'yes':
            activities = lifestyle_data.get('activitiesInfo', '').lower()
            # Check for extremely high-risk activities
            extreme_activities = ['skydiving', 'base jumping', 'motor racing', 'mountaineering']
            for activity in extreme_activities:
                if activity in activities:
                    return 100  # Immediate refer
            return 50  # High risk but not immediate refer
        else:
            return 0
    
    @staticmethod
    def _calculate_driving_score(lifestyle_data):
        """Calculate risk score based on driving history."""
        score = 0
        
        licence_status = lifestyle_data.get('licenceStatus', 'full')
        if licence_status in ['suspended', 'revoked']:
            score += 30
        
        convictions = lifestyle_data.get('convictions', 'no')
        if convictions == 'yes':
            score += 20
        
        accidents = lifestyle_data.get('accidents', 'no')
        if accidents == 'yes':
            score += 15
        
        return score
    
    @staticmethod
    def _calculate_criminal_score(financial_data):
        """Calculate risk score based on criminal history."""
        criminal = financial_data.get('criminalHistory', 'no')
        
        if criminal == 'yes':
            return 50
        else:
            return 0
    
    @staticmethod
    def _calculate_declination_score(financial_data):
        """Calculate risk score based on previous insurance declinations."""
        declination = financial_data.get('previousDeclination', 'no')
        
        if declination == 'yes':
            return 40
        else:
            return 0
    
    @staticmethod
    def _determine_decision(score):
        """Determine application decision based on total risk score."""
        if score >= 100:
            return 'REFER'
        elif score >= 60:
            return 'REFER'
        elif score >= 30:
            return 'ACCEPT_WITH_LOADING'
        else:
            return 'ACCEPT'
    
    @staticmethod
    def _get_risk_level(score):
        """Get risk level description based on score."""
        if score >= 100:
            return 'Very High Risk'
        elif score >= 60:
            return 'High Risk'
        elif score >= 30:
            return 'Moderate Risk'
        else:
            return 'Low Risk'
