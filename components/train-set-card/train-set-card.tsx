import styles from "./train-set-card.module.css";

type TrainSetCardProps = {
  title: string;
  description: string;
  className?: string;
};

export function TrainSetCard({ title, description, className }: TrainSetCardProps) {
  return (
    <div className={`${styles.card} ${className ?? ""}`}>
      <span className={styles.title}>{title}</span>
      <div className={styles.divider} />
      <p className={styles.description}>{description}</p>
    </div>
  );
}
